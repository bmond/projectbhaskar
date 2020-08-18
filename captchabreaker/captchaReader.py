from captcha_solver import CaptchaSolver

#solver = CaptchaSolver('browser')
solver = CaptchaSolver('antigate', api_key='ANTIGATE_KEY')
with open('captcha.png', 'rb') as inp:
    raw_data = inp.read()
print(solver.solve_captcha(raw_data))
