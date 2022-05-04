#!/usr/bin/env python
"""
Module to upload artifacts to W&B
Author : Yoovraj
Date : May 2022
"""

# import libraries
import logging
import argparse
import wandb

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def upload_artifactory(args):
    logger.info("Creating run exercise_1")
    with wandb.init(project="testing", group="group_1") as run:
        logger.info("Creating artifact")
        artifact = wandb.Artifact(
            name=args.artifact_name,
            type=args.artifact_type,
            description=args.artifact_description
        )
        artifact.add_file(args.input_file)
        logger.info("Logging artifact")
        run.log_artifact(artifact)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload artifactory tool")
    parser.add_argument(
        "--input_file",
        type=str,
        help="the path to an input file that will be uploaded as artifact",
        required=True)
    parser.add_argument(
        "--artifact_name",
        type=str,
        help="the name to be used for the artifact",
        required=True)
    parser.add_argument(
        "--artifact_type",
        type=str,
        help="the type of the artifact",
        required=True)
    parser.add_argument(
        "--artifact_description",
        type=str,
        help="a description for the artifact Inside the script you will find instructions about what to do",
        required=True)

    args = parser.parse_args()
    upload_artifactory(args)
