import cx_Freeze
exe = [cx_Freeze.Executable("maajiik.py")]
cx_Freeze.setup( name = "maajiik",
                version = "1.0",
                options = {"build_exe": {"packages": ["errno", "os", "re", "stat", "subprocess","collections","pprint","shutil"], "include_files": []}},
                executables = exe)