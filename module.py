#!/usr/bin/
class blados:
    import os
    def echo(x):
        print(x)
    e = echo
    def force(f):
        os.remove(f)
    f = force
    def remove(d):
        os.rmdir()
    r = remove
    def delete(d, a):
        if a == yes:
            shutil.rmtree(d)
        else:
            print("Not removing directory {1} and all of its contents.".format(d))
    d = delete
    def aa(p):
        pathlib.Path.unlink(p)
    a = aa
    def ww(p):
        pathlib.Path.rmdir()
    w = ww
    def copy(file):
        os.popen("cp {1}".format(file))
    c = copy
    def open(file):
	    open(file, "a")
    o = open
    def close(file):
        close(file)
    cl = close