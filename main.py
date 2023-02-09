import AminoXZ
import secmail
from time import sleep
from colored import fore
from random import choice
from string import ascii_letters
from os import system as shell
from requests import post
import traceback
from datetime import datetime

class Generator:
	def __init__(self, acc_file: str = 'accounts.txt', password: str = 'some-password', name_refix: str = 'XsarzBest-Bot', debug: bool = False):
		self.acc_file = acc_file
		self.password = password
		self.sec_mail = secmail.SecMail()
		self.name_refix = name_refix
		self.debug = debug

		self.colors = {
			'magenta': fore.LIGHT_MAGENTA,
			'blue': fore.DEEP_SKY_BLUE_2,
			'red': fore.RED,
			'white':fore.WHITE,
			'green':fore.GREEN
		}
		self.logo = f"""

		{self.colors['magenta']}


		╭━━╮╱╱╱╭━━╮
		┃╭╮┣━┳━┫╭━╋━┳━┳╮
		┃┣┫┃━┫━┫╰╮┃┻┫┃┃┃
		╰╯╰┻━┻━┻━━┻━┻┻━╯
			for amino.

			{self.colors['red']}
			Made By Xsarz -> @DXsarz
			{self.colors['blue']}
			GitHub: https://github.com/xXxCLOTIxXx
			Telegram channel: https://t.me/DxsarzUnion
			YouTube: https://www.youtube.com/channel/UCNKEgQmAvt6dD7jeMLpte9Q
			Discord server: https://discord.gg/GtpUnsHHT4
			{self.colors['white']}
		"""

	def GetVerifiCode(self, sec_mail, email: str):
		sleep(3)
		id_ = sec_mail.get_messages(email=email).id
		link_ = sec_mail.read_message(email, id_[0]).htmlBody.split('"')[13]
		return link_

	def accSave(self, email: str, password: str, deviceId: str):
		with open(self.acc_file, "a") as file:
			file.write(f"{email} {password} {deviceId}\n")

	def genName(self):return f'{self.name_refix}-{"".join([choice(ascii_letters) for i in range(12)])}'

	def date_now(self): return str(datetime.now())

	def getCapcha(self, url):
		req = post("https://captcha-solver-iukzq.run-eu-central1.goorm.app/predict", json={"url": url})
		return req.json()['prediction']


	def main(self):
		shell('cls || clear')
		print(self.logo)
		while True:
			deviceId = AminoXZ.lib.util.generator.Generator().generateDeviceId()
			client = AminoXZ.Client(deviceId=deviceId)
			try:
				nickname = self.genName()
				email = self.sec_mail.generate_email()
				client.request_verify_code(email=email)
				print(f'{self.colors["blue"]}\n[{self.date_now()}] [{email}]#~ {self.colors["magenta"]}Confirmation letter sent to email.')
				link = self.GetVerifiCode(sec_mail=self.sec_mail, email=email)
				print(f'{self.colors["blue"]}\n[{self.date_now()}] [{email}]#~ {self.colors["magenta"]}Capcha Link: {link}')
				verification_code = self.getCapcha(url=link)
				print(f'{self.colors["blue"]}\n[{self.date_now()}] [{email}]#~ {self.colors["magenta"]}Capcha code: {verification_code}')
				client.register(nickname=nickname, email=email, password=self.password, verificationCode=verification_code, deviceId=deviceId)
				print(f'{self.colors["blue"]}\n[{self.date_now()}] [{email}]#~ {self.colors["magenta"]} Account registered.')
				self.accSave(email=email, password=self.password, deviceId=deviceId)
				print(f'{self.colors["blue"]}\n[{self.date_now()}] [{email}]#~ {self.colors["green"]} Account  Saved.')
			except AminoXZ.lib.util.exceptions.InvalidVerificationCode:print(f'{self.colors["blue"]}\n[{self.date_now()}] [{email}]#~ {self.colors["red"]} Invalid verification code.')
			except AminoXZ.lib.util.exceptions.CommandCooldown:print(f'{self.colors["blue"]}\n[{self.date_now()}] [{email}]#~ {self.colors["red"]} The server rejected the registration request, try running the script later.');exit(0)
			except:print(f'{self.colors["blue"]}\n[{email}]#~ {self.colors["red"]} An error occurred while trying to register an account.\n{traceback.format_exc() if self.debug else ""}')

if __name__ == '__main__':
	Generator(password='t_me_DxsarzUnion', name_refix='XsarzBest').main()