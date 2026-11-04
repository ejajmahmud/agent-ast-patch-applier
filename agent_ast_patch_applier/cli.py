"""CLI for agent-ast-patch-applier."""
import sys
import argparse
from .applier import ASTPatchApplier


def main():
    parser = argparse.ArgumentParser(description="Agent AST Patch Applier")
    parser.add_argument("--demo", action="store_true", help="Run patch demo")
    args = parser.parse_args()

    applier = ASTPatchApplier()
    orig = "def hello():\n    print('world')\n"
    res, status = applier.apply_patch(orig, "print('world')", "print('universe')")
    print(f"Patch status: {status}\nResult:\n{res}")
    sys.exit(0)


if __name__ == "__main__":
    main()
