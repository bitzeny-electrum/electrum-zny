from pythonforandroid.recipe import CythonRecipe
from pythonforandroid.toolchain import current_directory
import shutil
import glob

class Zny_Yespower_0_5Recipe(CythonRecipe):

    url = 'https://github.com/bitzeny-electrum/zny_yespower_0_5_python3/archive/master.zip'

    patches = ['./setup.patch']
    depends = ['setuptools']

#    def build_arch(self, arch):
#        super(Zny_Yespower_0_5Recipe, self).build_arch(arch)
#
#        env = self.get_recipe_env(arch)
#        with current_directory(self.get_build_dir(arch.arch)):
#            so_file = glob.glob('./build/lib*/*so')
#            shutil.copyfile(so_file[0], self.ctx.get_libs_dir(arch.arch) + "/zny_yespower_0_5.so")

recipe = Zny_Yespower_0_5Recipe()
