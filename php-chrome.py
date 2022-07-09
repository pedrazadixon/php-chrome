import os
import subprocess
import shutil
import tempfile

# paths
work_dir = os.getcwd()
chromium_bin = os.path.join(work_dir, 'chrome-bin', 'chrome.exe')
php_bin = os.path.join(work_dir, 'php-bin', 'php.exe')
www_dir = os.path.join(work_dir, 'www')
profile_directory = os.path.join(tempfile.gettempdir(), 'php-chrome-profile')

# start php server
php_server = subprocess.Popen(
    php_bin + ' -S ' + '127.0.0.1:8001' + ' -t ' + www_dir)

# start chromiun and wait
chromium_args = [
    '--new-window',
    '--window-size=980,600',
    '--disable-extensions',
    '--disable-features=Translate',
    '--disable-sync',
    '--user-data-dir="' + profile_directory + '"']

chromium_string_args = ' '.join(chromium_args)

chrome_process = subprocess.Popen(
    chromium_bin + ' ' + chromium_string_args + ' --app=' + '"http://127.0.0.1:8001"').wait()

# end program and cleanup
php_server.kill()
shutil.rmtree(profile_directory)
