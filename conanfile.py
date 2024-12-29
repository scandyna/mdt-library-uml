from conan import ConanFile
from conan.tools.env import VirtualBuildEnv
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake

# NOTE: this recipe is only to install dependnecies.
class MdtLibraryUmlConan(ConanFile):
  name = "mdtlibraryuml"
  #version = "0.1"
  license = "BSD 3-Clause"
  url = "https://gitlab.com/scandyna/mdt-library-uml"
  description = "UML for multidiagtools library."
  settings = "os", "compiler", "build_type", "arch"
  generators = "CMakeDeps", "CMakeToolchain", "VirtualBuildEnv"

  def build_requirements(self):
    self.test_requires("mdtcmakemodules/0.20.0@scandyna/testing")
