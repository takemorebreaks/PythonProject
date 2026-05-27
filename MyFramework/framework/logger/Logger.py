import logging
import os


class Logger:
    @staticmethod
    def get_logger(name="FrameworkLogger"):
        # Create logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            # Console handler
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            # File handler
            log_dir = "reports/logs"
            os.makedirs(log_dir, exist_ok=True)
            fh = logging.FileHandler(os.path.join(log_dir, "framework.log"), mode="a")
            fh.setLevel(logging.DEBUG)

            # Formatter
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            ch.setFormatter(formatter)
            fh.setFormatter(formatter)

            # Add handlers
            logger.addHandler(ch)
            logger.addHandler(fh)

        return logger