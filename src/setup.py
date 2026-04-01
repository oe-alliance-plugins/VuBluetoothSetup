from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.VuBluetoothSetup'
setup(name='enigma2-plugin-systemplugins-bluetoothsetup',
       version='3.0',
       description='VuPLus bluetooth plugin',
       package_dir={pkg: 'VuBluetoothSetup'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'plugin.png', 'bt_audio.png', 'bt_keyboard.png', 'bt_misc.png', 'bt_rc.png', 'keymap.xml', 'vu_rcu_firmware.bin']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
