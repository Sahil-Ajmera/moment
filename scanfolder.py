import os
import os.path
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description="Welcome to slides helper!")
    parser.add_argument('--scan-me',
                        nargs='?',
                        required=True,
                        help="Folder to scan.")

    args = parser.parse_args()

    images = []
    root = os.path.join(".", args.scan_me)
    for dirpath, dirnames, filenames in os.walk(root):
        for f in filenames:
            name, ext = os.path.splitext(f)
            if ext.lower() in [".png", ".jpg", ".jpeg"]:
                full_path = os.path.join(dirpath, f)

                # we remove root from path since generated `.md`
                # will be used inside the `root` folder, so everything
                # is relative below it.
                images.append(full_path.replace(root + os.path.sep, ""))

    template = """
---
<h6>%s</h6>
<img data-src="%s"
     class="responsive-img materialboxed"
     style="box-shadow:none;">
    """
    with open("%s.md" % args.scan_me, "w") as f:
        for m in images:
            f.write(template % (os.path.split(m)[-1], m))


if __name__ == "__main__":
    main()
