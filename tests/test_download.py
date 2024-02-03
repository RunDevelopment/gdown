import os
import tempfile

from gdown.download import download


def test_download():
    url = "https://raw.githubusercontent.com/wkentaro/gdown/3.1.0/gdown/__init__.py"  # NOQA

    with tempfile.TemporaryDirectory() as d:
        output = os.path.join(d, "gdown_r")
        # Usage before https://github.com/wkentaro/gdown/pull/32
        assert download(url, output, quiet=False) == output
        os.remove(output)
