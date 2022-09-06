import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os.path

import logging
logger = logging.getLogger('root')
logger.setLevel('INFO')

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, help="tracking dir")
parser.add_argument("-o", "--output", type=str, help="destination dir")
args = parser.parse_args()

from PIL import Image


# Listening for new files
def on_created(event):
    logger.warning(f"{event.src_path} has been created, processing...")

    img = Image.open(event.src_path)

    # Proceccing...
    img = img.transpose(Image.FLIP_TOP_BOTTOM)

    output_path = os.path.join(args.output, os.path.basename(event.src_path))
    img.save(output_path)
    logger.warning(f"Finished. Result saved to {output_path}.")


if __name__ == "__main__":
    patterns = ["*.png"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True

    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created

    input_path = args.input

    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, input_path, recursive=go_recursively)
    my_observer.start()
    logger.warning(f"Observer started!")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
