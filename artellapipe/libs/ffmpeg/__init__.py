import os
import logging

LOGGER = logging.getLogger()


def get_ffmpeg_executable():
    """
    Returns path where FFMpeg executable is located
    :return: str
    """

    from tpPyUtils import path, osplatform

    externals_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'externals')
    if not externals_dir or not os.path.isdir(externals_dir):
        LOGGER.warning('No externals directory found: "{}"'.format(externals_dir))
        return

    platform_name = osplatform.get_platform().lower()
    os_architecture = osplatform.get_architecture()

    ffmpeg_exe_path = path.clean_path(os.path.join(externals_dir, platform_name, os_architecture, 'bin', 'ffmpeg.exe'))
    if not os.path.isfile(ffmpeg_exe_path):
        LOGGER.warning('No FFMpeg executable file found in path: "{}"'.format(ffmpeg_exe_path))
        return None

    return ffmpeg_exe_path
