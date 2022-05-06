# __main__ is not required for DALiuGE components.
import argparse  # pragma: no cover

from . import MonteCarloDROP  # pragma: no cover


def main() -> None:  # pragma: no cover
    """
    The main function executes on commands:
    `python -m dlg_monte_carlo` and `$ dlg_monte_carlo `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    parser = argparse.ArgumentParser(
        description="dlg_monte_carlo.",
        epilog="Enjoy the dlg_monte_carlo functionality!",
    )
    # This is optional named argument
    parser.add_argument(
        "-N",
        "--numtrials",
        type=int,
        help="The number of darts to throw",
        default=10000,
        required=False,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Optionally adds verbosity",
    )
    args = parser.parse_args()
    if args.verbose:
        print("Verbose mode is on.")

    print("Executing main function")
    comp = MonteCarloDROP(oid='a', uid='a', numtrials=args.numtrials)
    comp.run()
    print("End of main function")


if __name__ == "__main__":  # pragma: no cover
    main()
