import sys

if "travis_deploy" not in sys.argv:
    raise ValueError("Setup file is written to support travis publish.")
import build_packages

sys.exit(build_packages.travis_build_package())
