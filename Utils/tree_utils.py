#!/usr/bin/env python3
'''
Requirements:

Python Packages:
dendropy
ete3

On Path:
fitch.linux (from TreeFixVP)
'''
import sys, os, re
import dendropy as dp
import ete3 as ete
import subprocess as sp
import numpy as np

def root(tf):
    tree = dp.Tree.get(path=tf, schema='newick', rooting='force-rooted')
    tree.is_rooted = True
    tree.reroot_at_midpoint()
    tree.update_bipartitions(suppress_unifurcations=False)
    tree.write(path=tf, schema='newick', suppress_rooting=True)
    return "Done"

def unroot(tf):
    tree = ete.Tree(tf)
    tree.unroot()
    tree.write(tf)
    return "Done"

def show(tf):
    try:
        os.environ['DISPLAY']
        from ete3 import TreeStyle
        flag = 0
    except (KeyError, ImportError):
        flag = 1
    if flag:
        tree = dp.Tree.get(path=tf, schema='newick', rooting='force-rooted')
        print(tree.as_ascii_plot())
    else:
        tree = ete.Tree(tf)
        ts = TreeStyle()
        ts.show_leaf_name = True
        ts.show_branch_length = True
        ts.scale = 25
        tree.show(tree_style=ts)
    return "Done"

def leaves(tf):
    tree = ete.Tree(tf)
    return len(tree.get_leaves())

def rf(tf, tf2=None):
    t1 = ete.Tree(tf)
    if tf2 is None:
        try:
            tf2 = sys.argv[3]
            t2 = ete.Tree(tf2)
            print("Tree File 2 = {}".format(tf2))
        except(IndexError):
            short_help()    
    else:
        t2 = ete.Tree(tf2)
    t1.unroot()
    t2.unroot()
    return int(t1.robinson_foulds(t2, unrooted_trees=True)[0] / 2)

def fitch(tf):
    child = sp.Popen(["fitch.linux", tf], stdout=sp.PIPE)
    result = child.communicate()[0][:-1].decode('utf-8')
    child.wait()
    if child.returncode:
        print("Fitch.linux was unable to read the given file. It may not exist or is malformed.")
        sys.exit(1)
    return(result)

def branch_lengths(tf):
    with open(tf, 'r') as f:
        tree = f.read()
    compiled = re.compile(r":([0-9]+\.[0-9]+)")
    #compiled = re.compile(r"\b[0-9]+(?:\.[0-9]+)?\b")
    br_lens = [float(i[1:]) for i in compiled.findall(tree)]
    br_lens.sort()
    summary = { "branch_lengths": br_lens,
                "shortest": min(br_lens),
                "25percentile": br_lens[int(len(br_lens)*0.25)],
                "mean": np.mean(br_lens),
                "75percentile": br_lens[int(len(br_lens)*0.75)],
                "longest": max(br_lens),
    }
    try:
        os.environ['DISPLAY']
        from matplotlib import pyplot as plt
        flag = 0
    except (KeyError, ImportError):
        flag = 1
    if flag or __name__ != '__main__':
        return summary
    else:
        min_ = br_lens[np.nonzero(br_lens)[0][0]]
        f = plt.figure()
        ax = f.add_subplot(111)
        plt.hist(br_lens, bins=np.logspace(np.log10(min_), np.log10(summary["longest"]), 50))
        plt.xscale('log')
        plt.text(0.05,0.75,'Min: {}\n25 Percentile: {}\nMean: {}\n75 Percentile: {}\nMax: {}'.format(summary["shortest"], summary["25percentile"], summary["mean"], summary["75percentile"], summary["longest"]), transform=ax.transAxes)
        plt.title("Branch Length Distribution for {}".format(tf))
        plt.show()
        return "Done"
        
def nexus(tf):
    t = ete.Tree(tf)
    tree_name = tf.split('/')[-1]
    with open('{}.NEXUS'.format(tree_name), 'w+') as f:
        f.write("#NEXUS\nBEGIN TREES;\n")
        f.write("tree {} = {}\n".format(tree_name, t.write()))
        f.write("END;")
    return "Done"

def short_help():
    print("Usage: ./tree_utils [operation] [tree path] [optional second tree]")
    print("Operations: '{}'".format("', '".join(ops_dict)))
    sys.exit(1)

def long_help():    
    print("Usage: ./tree_utils [operation] [tree path] [optional second tree]\n")
    print("root: roots given tree")
    print("unroot: unroots given tree")
    print("show: displays given tree using ete tree viewer or ascii representation")
    print("leaves: returns the number of leaves in given tree")
    print("rf: returns the unrooted Robinson-Foulds distance between two given trees")
    print("fitch: calculates minimum transmission score using Fitch's algorithm")
    print("brlen: returns summary of branch lengths within given tree")
    print("nexus: write newick tree as nexus file")
    print("help: displays this message")
    sys.exit(1)

def main():
    
    try:
        op = sys.argv[1]
    except:
        short_help()
    if op == "help":
        long_help()
    try:
        tf = sys.argv[2]
    except:
        short_help()

    print("Operation = {}".format(op))
    print("Tree File = {}".format(tf))

    print(ops_dict.get(op, lambda x: 'Invalid Operation')(tf))

if __name__ == "__main__":
    ops_dict = {
        "root": root,
        "unroot": unroot,
        "show": show,
        "leaves": leaves,
        "rf": rf,
        "fitch": fitch,
        "brlen": branch_lengths,
        "nexus": nexus,
        "help": long_help
      }
    main()
