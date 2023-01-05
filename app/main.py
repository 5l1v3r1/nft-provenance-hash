import os
import hashlib
from loguru import logger


class ProvenanceHash:
    def __init__(self) -> None:
        pass

    @staticmethod
    def read_image_bytes(image_path: str):
        """
        Read image bytes from a file path
        :param image_path: path to image file
        :return: bytes of image
        """
        try:
            logger.info(f"Reading image bytes from {image_path}")
            with open(image_path, "rb") as f:
                return f.read()

        except Exception as e:
            print(e)
            return None

    @staticmethod
    def get_hash(image_bytes: bytes):
        """
        Get the hash of the image bytes
        :param image_bytes: bytes of image
        :return: hash of image bytes
        """
        try:
            logger.info(f"Getting hash of image bytes")
            return hashlib.sha256(image_bytes).hexdigest()

        except Exception as e:
            print(e)
            return None

    def get_provenance_hash(self, image_path: str):
        """
        Get the provenance hash of an image
        :param image_path: path to image
        :return: provenance hash of image
        """
        try:
            logger.info(f"Getting provenance hash of image at {image_path}")
            image_bytes = self.read_image_bytes(image_path)
            return self.get_hash(image_bytes)

        except Exception as e:
            print(e)
            return None

    def get_multiple_provenance_hashes(self, directory_path: list):
        """
        Get the provenance hashes of multiple images
        :param directory_path: path to directory containing images
        :return: provenance hashes of images
        """
        try:
            logger.info(f"Getting provenance hashes of images in {directory_path}")
            provenance_hashes = {}
            for filename in os.listdir(directory_path):
                image_path = os.path.join(directory_path, filename)
                provenance_hashes[filename] = self.get_provenance_hash(image_path)
            # provenance_hashes["hashes"] = provenance_hashes.values()
            return provenance_hashes

        except Exception as e:
            print(e)
            return None
