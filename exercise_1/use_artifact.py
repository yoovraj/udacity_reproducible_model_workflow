#!/usr/bin/env python
"""
Module to use artifacts to W&B
Author : Yoovraj
Date : May 2022
"""
import argparse
import logging
import wandb


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def use_artifact(args):

    logger.info("Creating run in project exercise_1")
    with wandb.init(project="testing", group="group_1") as run:
        logger.info("Getting artifact")
        artifact = run.use_artifact(args.artifact_name)
        artifact_path = artifact.file()

        logger.info(f"Artifact content: {artifact_path}")
        with open(artifact_path, "r") as fp:
            content = fp.read()

        print(content)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="Use an artifact from W&B", 
        fromfile_prefix_chars="@"
    )

    parser.add_argument(
        "--artifact_name", 
        type=str, 
        help="Name and version of W&B artifact", 
        required=True
    )

    args = parser.parse_args()

    use_artifact(args)