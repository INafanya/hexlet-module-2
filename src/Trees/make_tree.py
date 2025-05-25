from hexlet_fs import mkdir, mkfile


# BEGIN (write your solution here)
def generate():
    tree = mkdir("python-package", 
        children = [
            mkfile("Makefile"),
            mkfile("README.md"),
            mkdir("dist", []),
            mkdir("tests",
                children = [
                    mkfile("test_solution.py")
                ]
            ),
            mkfile("pyproject.toml"),
            mkdir(".venv",
                children = [
                    mkdir("lib",
                        children = [
                            mkdir("python3.6",
                               children = [
                                    mkdir("site-packages",
                                        children = [
                                            mkfile("hexlet-python-package.egg-link")
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                ],
                meta = {'owner': 'root', 'hidden': False}
            )
        ],
        meta = {'hidden': True}
    )
    return tree
# END
