#!/usr/bin/python
"""Main script for python boilerplate."""
import argparse
import os


def main(client_id, client_secret):
    """Fetch main data."""
    assert len(client_secret) > 0
    print(f"Using {client_id}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python Boilerplate.",
        add_help=True,
    )
    parser.add_argument(
        "--client_id",
        "-c",
        help="Application Client Id",
    )
    parser.add_argument(
        "--client_secret",
        "-s",
        help="Application Client Secret",
    )
    args = parser.parse_args()

    CLIENT_ID = args.client_id or os.environ.get("CLIENT_ID")
    CLIENT_SECRET = args.client_secret or os.environ.get("CLIENT_SECRET")

    if not CLIENT_ID:
        raise ValueError(
            "Client Id name is required. Have you set the CLIENT_ID env variable?"
        )

    if not CLIENT_SECRET:
        raise ValueError(
            "Client Secret name is required."
            "Have you set the CLIENT_SECRET env variable?"
        )

    main(CLIENT_ID, CLIENT_SECRET)
