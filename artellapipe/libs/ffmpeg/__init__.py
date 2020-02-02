import os
import sys
import logging

LOGGER = logging.getLogger()


def get_ffmpeg_executable():
    """
    Returns path where FFMpeg executable is located
    :return: str
    """

    from tpPyUtils import path, osplatform

    externals_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'externals', 'exe')
    if not externals_dir or not os.path.isdir(externals_dir):
        LOGGER.warning('No externals directory found: "{}"'.format(externals_dir))
        return

    platform_name = osplatform.get_platform().lower()
    os_architecture = osplatform.get_architecture()

    ffmpeg_exe_path = path.clean_path(
        os.path.join(externals_dir, platform_name, os_architecture, 'ffmpeg', 'bin', 'ffmpeg.exe'))
    if not os.path.isfile(ffmpeg_exe_path):
        LOGGER.warning('No FFMpeg executable file found in path: "{}"'.format(ffmpeg_exe_path))
        return None

    return ffmpeg_exe_path


def get_pil_lib():
    """
    Returns path where PIL lib for current DCC is located
    :return: str
    """

    import tpDccLib as tp
    from tpPyUtils import path

    externals_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'externals', 'lib')
    if not externals_dir or not os.path.isdir(externals_dir):
        LOGGER.warning('No externals directory found: "{}"'.format(externals_dir))
        return

    dcc_name = tp.Dcc.get_name()
    dcc_version = tp.Dcc.get_version_name()

    pil_lib_path = path.clean_path(os.path.join(externals_dir, dcc_name, dcc_version, 'pil'))
    if not os.path.isdir(pil_lib_path):
        LOGGER.warning('No PIL library directory found in path: "{}"'.format(pil_lib_path))
        return None

    return pil_lib_path


# We add PIL to sys.path if necessary ...
try:
    import PIL
except ImportError:
    pil_path = get_pil_lib()
    if pil_path and os.path.isdir(pil_path) and not pil_path in sys.path:
        LOGGER.debug('Adding PIL path to sys.path: {} ...'.format(pil_path))
        sys.path.append(pil_path)
