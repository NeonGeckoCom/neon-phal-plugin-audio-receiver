from neon_phal_plugin_audio_receiver.utils import read_file, write_to_file


def test_read_file(tmpdir):
    # Create a temporary file with some content
    file_path = tmpdir.join("test_file.txt")
    file_path.write("line1\nline2\n")

    content = read_file(file_path.strpath)
    assert content == ["line1\n", "line2\n"]


def test_write_to_file(tmpdir):
    content = ["line1\n", "line2\n"]
    file_path = tmpdir.join("test_file.txt")
    write_to_file(file_path.strpath, content)

    with open(file_path.strpath, "r", encoding="utf-8") as f:
        assert f.readlines() == content
