import os
import re
import shutil
import subprocess
import traceback
import requests

class ReleaseManager:
    def __init__(self):
        self.setup = self.getSetup()
        self.changelog = self.getChangelog()

    def getSetup(self):
        with open("setup.py", "r+", encoding="utf-8") as f:
            setup = f.read()
            f.close()
        return setup

    def getChangelog(self):
        with open("CHANGELOG.md", "r", encoding="utf-8") as f:
            changelog = f.read()
            f.close()
        return changelog

    def updateSetup(self, newVersion):
        with open("setup.py", "w", encoding="utf-8") as f:
            newSetup = re.sub("version='.*'", "version='{}'".format(newVersion), self.setup)
            f.seek(0)
            f.truncate()
            f.write(newSetup)
            f.close()

    def revertSetup(self):
        with open("setup.py", "w", encoding="utf-8") as f:
            f.seek(0)
            f.truncate()
            f.write(self.setup)
            f.close()

    def updateChangelog(self, newVersion):
        with open("CHANGELOG.md", "w", encoding="utf-8") as f:
            newChangelog = self.changelog.replace("[Unreleased ({})]".format(newVersion), "[{}]".format(newVersion))
            f.seek(0)
            f.truncate()
            f.write(newChangelog)
            f.close()

    def revertChangelog(self):
        with open("CHANGELOG.md", "w", encoding="utf-8") as f:
            f.seek(0)
            f.truncate()
            f.write(self.changelog)
            f.close()

    def getUnreleasedVersion(self):
        with open("CHANGELOG.md", "r", encoding="utf-8") as f:
            changelog = f.read()
            unreleased = re.search("\[Unreleased.*\]", changelog).group(0)
            version = re.search("\(.*\)", unreleased).group(0)[1:-1]
            f.close()
        return version

    def release(self):
        try:
            version = self.getUnreleasedVersion()
            self.updateSetup(version)
            self.updateChangelog(version)
            if os.path.isdir("dist"): shutil.rmtree("dist")
            subprocess.call('py -m pip install build twine')
            subprocess.call('py setup.py sdist')
            subprocess.call('py -m twine upload -r qwertypy dist/*')
            subprocess.call('git add .')
            subprocess.call('git commit -m "Released version {}"'.format(version))
        except Exception as e:
            print(traceback.format_exc())
            self.revertSetup()
            self.revertChangelog()
            print("Failed to release version {}!".format(version))


releaseManager = ReleaseManager()
releaseManager.release()
