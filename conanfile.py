from conans import ConanFile, tools
import os

# NOTE: this recipe is only to install dependnecies.
class MdtLibraryUmlConan(ConanFile):
  name = "mdt-library-uml"
  #version = "0.1"
  license = "BSD 3-Clause"
  url = "https://gitlab.com/scandyna/mdt-library-uml"
  description = "UML for multidiagtools library."
  settings = "os", "compiler", "build_type", "arch"
  generators = "CMakeDeps", "CMakeToolchain", "VirtualBuildEnv"

  # When using --profile:build xx and --profile:host xx ,
  # the dependencies declared in build_requires and tool_requires
  # will not generate the required files.
  # see:
  # - https://github.com/conan-io/conan/issues/10272
  # - https://github.com/conan-io/conan/issues/9951
  def build_requirements(self):
    # Due to a issue using GitLab Conan repository,
    # version ranges are not possible.
    # See https://gitlab.com/gitlab-org/gitlab/-/issues/333638
    self.tool_requires("MdtCMakeModules/0.19.3@scandyna/testing", force_host_context=True)
