# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.15)

# CMAKE_PREFIX_PATH is empty before any call to project()
# Because set_project_version() does not exist,
# we call the project command twice (is there a cleaner solution?)
project(MdtLibraryUml)

#######################################################
# Project definition with versionning got from git tag
#######################################################

find_package(Git REQUIRED)
find_package(MdtCMakeModules REQUIRED)

message(DEBUG "MDT_CMAKE_MODULES_PATH: ${MDT_CMAKE_MODULES_PATH}")

include(MdtVersionUtils)

set(INITIAL_PROJECT_VERSION)
if(FROM_CONAN_PROJECT_VERSION)
  set(INITIAL_PROJECT_VERSION ${FROM_CONAN_PROJECT_VERSION})
else()
  mdt_cmake_project_version_from_git_tag(INITIAL_PROJECT_VERSION DEFAULT_VERSION 0.0.0)
endif()

project(MdtLibraryUml VERSION ${INITIAL_PROJECT_VERSION} LANGUAGES NONE)

unset(INITIAL_PROJECT_VERSION)


#######################
# Dependencies
#######################

include(FindDoxygen)
find_package(Doxygen REQUIRED dot)


#######################
# Sources
#######################

add_subdirectory(doxygen-view)
