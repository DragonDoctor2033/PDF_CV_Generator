from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.layout.image.barcode import Barcode, BarcodeType, Image
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout, Document
from borb.pdf.canvas.layout.text.paragraph import Paragraph, Alignment, Decimal, ChunkOfText, Page
from borb.pdf.pdf import PDF

pdf = Document()
page = Page()
pdf.append_page(page)

# Create dictionary, where store text to add in file
dict_list = {
    'Bio_Info':
        {
            1: "I want to find job in your company!\nSome info about me:",
            2: " English: B2. "
               "\nDon't have a higher degree, only school 12 years. "
               "\nRight now work at Transcom, as Senior Technical Advisor. "
               "\nI've created this CV only using Python ",
        },
    'Work_Experience':
        {
            1: 'Transcom.',
            2:  'Right now work as the senior technical advisor. My responsibilities: \n\n'
                'Receive calls from the 1st line of support and end-users. Provide consultations, how to resolve issues'
                ', and, if unable to resolve during the interaction, create requests to the engineers and '
                'resolve issues with them.',
            3: 'Shortcut.',
            4: ' From August 2018 to September 2019 worked as a video engineer. Leave job by myself, because of '
               'my comeback to Estonia. My responsibilities:\n\n Receive calls, emails, and tasks in Zendesk from '
               'the customers. Most of the time resolve issues with the macOS, Windows 10, and Synology. '
               'Create users, set up corporate mail, set up VPN, add in Active Directory / Open Directory. '
               'Sometimes, configure Zabbix on Raspberry Pi, contact with the ISP or with Service Centers '
        },
    'Hobbies':
        {
            1: "I love to learn everything new in IT. Because I have a personal server for Plex and Searx was need "
               "to open them from an external network, for this reason, bought a domain and using Raspberry create a"
               " reverse proxy and now able to open them not only from the local network.\n\n To get access to my local"
               " network configured VPN and use my domain name, to connect to it.\n\n As you can see, "
               "right now learn Python. For my personal reasons create Telegram Bot, which can receive the audio "
               "message and send text from the audio. 2nd bot was created to store customer's data when giving devices "
               "to the repair. Both of them can be found on my GitHub page. "
        }
}

# Put photo on background, to leave text in correct position
Photo_CV = SingleColumnLayout(page)

for _ in range(3):
    Photo_CV.add(Paragraph(' '))

Photo_CV.add(Image('https://media-exp1.licdn.com/dms/image/C4E03AQHrwOm1Afls8w'
                   '/profile-displayphoto-shrink_800_800/0/1623235494628?e=1634169600&v='
                   'beta&t=5JkrDibgKl-wlX21lLAknB9WrQMgoP4WQzFSLO6wfhI', width=Decimal(125), height=Decimal(125)))

# Create new layer, to write main text.
Bio_Info = SingleColumnLayout(page)

Bio_Info.add(Paragraph('Anatoly Tarakanovskiy', font_size=Decimal(30))) \
    .add(Paragraph('Hello!', horizontal_alignment=Alignment.RIGHT))

for i in dict_list['Bio_Info']:
    Bio_Info.add(Paragraph(text=dict_list['Bio_Info'][i],
                           horizontal_alignment=Alignment.RIGHT,
                           font_size=Decimal(11),
                           text_alignment=Alignment.RIGHT,
                           respect_newlines_in_text=True))

ChunkOfText('23 Years Old', horizontal_alignment=Alignment.CENTERED, font_size=Decimal(13)).layout(
    page, Rectangle(
        lower_left_x=Decimal(225),
        lower_left_y=Decimal(667),
        width=Decimal(10),
        height=Decimal(10)))
# Create layer about work experience.
work_exp = SingleColumnLayout(page)
ChunkOfText('My work experience:', font='Helvetica-Bold').layout(page, Rectangle(lower_left_x=Decimal(60),
                                                                                 lower_left_y=Decimal(535),
                                                                                 width=Decimal(10),
                                                                                 height=Decimal(10)))
for _ in range(9):
    work_exp.add(Paragraph(' '))
for i in dict_list['Work_Experience']:
    if i % 2 != 0:
        work_exp.add(Paragraph(text=dict_list['Work_Experience'][i],
                               horizontal_alignment=Alignment.LEFT,
                               font_size=Decimal(12),
                               respect_newlines_in_text=True,
                               font='Helvetica-Bold', ))
        continue
    work_exp.add(Paragraph(text=dict_list['Work_Experience'][i],
                           horizontal_alignment=Alignment.LEFT,
                           font_size=Decimal(11),
                           text_alignment=Alignment.LEFT,
                           respect_newlines_in_text=True))

# Create layer to print info about hobbies.

My_Hobbies = SingleColumnLayout(page)

for _ in range(19):
    My_Hobbies.add(Paragraph(' '))
ChunkOfText('Hobbies: ', font='Helvetica-Bold').layout(page, Rectangle(
    lower_left_x=Decimal(59),
    lower_left_y=Decimal(300),
    width=Decimal(10),
    height=Decimal(10)))
for i in dict_list['Hobbies']:
    My_Hobbies.add(Paragraph(dict_list['Hobbies'][i],
                             font_size=Decimal(10),
                             respect_newlines_in_text=True,))

# Create layer to print info about this code and print QR Code
code_source = SingleColumnLayout(page)

ChunkOfText('You can find code of this PDF using QR Code below',
            font_size=Decimal(10)) \
    .layout(page, Rectangle(lower_left_x=Decimal(175),
                            lower_left_y=Decimal(155),
                            width=Decimal(201),
                            height=Decimal(10)))

code_source.add(Barcode(data='https://github.com/DragonDoctor2033/PDF_CV_Generator/blob/main/main.py',
                        type=BarcodeType.QR,
                        horizontal_alignment=Alignment.CENTERED,
                        vertical_alignment=Alignment.BOTTOM,
                        height=Decimal(60),
                        width=Decimal(60)))

# store the PDF
with open("CV_Anatoly_Tarakanovskiy.pdf", "wb") as pdf_file_handle:
    PDF.dumps(pdf_file_handle, pdf)
