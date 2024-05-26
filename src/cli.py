from src.file_system import FileSystem

def main():
    fs = FileSystem()
    
    while True:
        try:
            command = input(f"{fs.current.name}> ").strip()
            if not command:
                continue

            if ">" in command:
                parts = command.split(">")
                cmd = parts[0].strip().split()
                if cmd[0] == "echo":
                    text = " ".join(cmd[1:])
                    filename = parts[1].strip()
                    fs.echo(filename, text)
                else:
                    print("Unknown command")
            else:
                parts = command.split()
                cmd = parts[0]
                args = parts[1:]

                if cmd == "mkdir":
                    fs.mkdir(args[0])
                elif cmd == "cd":
                    fs.cd(args[0])
                elif cmd == "ls":
                    fs.ls(args[0] if args else ".")
                elif cmd == "touch":
                    fs.touch(args[0])
                elif cmd == "cat":
                    print(fs.cat(args[0]))
                elif cmd == "rm":
                    fs.rm(args[0])
                elif cmd == "mv":
                    fs.mv(args[0], args[1])
                elif cmd == "cp":
                    fs.cp(args[0], args[1])
                elif cmd == "exit":
                    break
                else:
                    print("Unknown command")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
