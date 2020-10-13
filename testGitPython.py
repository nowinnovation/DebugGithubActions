import git

if __name__ == "__main__":
    triedAndTrue=True
    clone=git.Git(".")
    clone.clone("https://github.com/actions/starter-workflows",None,None,"--bare")
    assert(triedAndTrue)
