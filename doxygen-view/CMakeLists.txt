# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

############################
# Variables that are reused
# in the Doxyfiles
############################

# set(DOT_FILES_CMAKE_DIR "${CMAKE_CURRENT_BINARY_DIR}/dotfiles/cmake")

find_file(PLANTUML_JAR_PATH "plantuml.jar" PATHS "/usr/share/plantuml")
if(NOT EXISTS "${PLANTUML_JAR_PATH}")
  message(WARNING "plantuml.jar not found, UML diagrams will not be generated")
  set(PLANTUML_JAR_PATH "")
endif()

set(PLANTUML_INCLUDE_PATH "${PROJECT_SOURCE_DIR}/plantuml")


#######################
# Doxygen view
#######################

configure_file(
  "${PROJECT_SOURCE_DIR}/doxygen-view/Doxyfile.in"
  "${PROJECT_BINARY_DIR}/doxygen-view/Doxyfile"
)

add_custom_command(
    OUTPUT doxygen-view
    COMMAND
      Doxygen::doxygen "${PROJECT_BINARY_DIR}/doxygen-view/Doxyfile"
    COMMENT "Build Doxygen view"
    VERBATIM
)
set_property(SOURCE doxygen-view PROPERTY SYMBOLIC 1)
add_custom_target(DoxygenView ALL DEPENDS doxygen-view)
