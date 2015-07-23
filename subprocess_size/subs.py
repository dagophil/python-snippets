import sys
import subprocess


def main():
    cmd = ["python", "prog.py"]
    for i in xrange(100000):
        cmd.append(str(i).zfill(19))
    s = " ".join(cmd)
    print "cmd size:", len(s)
    subprocess.call(cmd)
    print "done"
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)
