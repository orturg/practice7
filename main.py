from app.io.input import read_from_console, read_from_file, read_from_file_pandas
from app.io.output import write_to_console, write_to_file


def main():
    file_to_read = "file1.txt"
    file_to_write = "file2.txt"

    text_console = read_from_console()
    text_file_builtin = read_from_file(file_to_read)
    text_file_pandas = read_from_file_pandas(file_to_read)

    write_to_console(text_console)
    write_to_console(text_file_builtin)
    write_to_console(text_file_pandas)

    write_to_file(file_to_write, text_console)
    write_to_file(file_to_write, text_file_builtin)
    write_to_file(file_to_write, text_file_pandas)

if __name__ == "__main__":
    main()



