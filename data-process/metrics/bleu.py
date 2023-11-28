import evaluate
bleu = evaluate.load('bleu')

# Japanese to English
lst = []
predictions=[
    "Xói mòn bề mặt và tổn thương niêm mạc có dấu lấm chấm xảy ra. Những điều này có thể xảy ra sớm nhất là 12 giờ sau chấn thương ban đầu. Trong những trường hợp nghiêm trọng hoặc không được điều trị, vết loét sâu, loét và đôi khi thủng có thể phát triển. Các tổn thương thường xảy ra ở phần thân dạ dày nhưng hang vị cũng có thể bị ảnh hưởng.".split(" "),
    "Viêm dạ dày căng thẳng cấp tính, một loại viêm dạ dày ăn mòn, xảy ra ở khoảng 5% bệnh nhân bị bệnh nặng. Tỷ lệ mắc bệnh tăng theo thời gian nằm ICU và thời gian bệnh nhân không được dinh dưỡng qua đường ruột. Cơ chế bệnh sinh có thể liên quan đến rối loạn chức năng bảo vệ niêm mạc do giảm lưu lượng máu đến niêm mạc đường tiêu hóa. Tăng tiết axit dạ dày cũng có thể thấy ở những bệnh nhân bị chấn thương đầu hoặc bỏng.".split(" ")
]
references=[
    [
        "Có vết trợt trên bề mặt và thương tổn xuyên qua lớp niêm mạc. Bệnh có thể tiến triển ngay sau 12 giờ tổn thương đầu tiên. Các vết trợt sâu, loét, và đôi khi thủng có thể xảy ra trong các trường hợp nặng hoặc không được điều trị. Các thương tổn thường xảy ra ở thân vị, nhưng hang bị cũng có thể bị ảnh hưởng.".split(" ")
    ],
    [
        "Viêm dạ dày cấp tính do căng thẳng, một dạng viêm dạ dày ăn mòn, xảy ra ở khoảng 5% số bệnh nhân nguy kịch. Tỷ lệ này tăng theo thời gian nằm viện của bệnh nhân ở khoa hồi sức tích cực và thời gian mà bệnh nhân không được nuôi ăn theo đường ruột. Nguyên nhân sinh bệnh có thể liên quan đến giảm tưới máu của niêm mạc đường tiêu hoá, dẫn đến suy yếu của hàng rào bảo vệ niêm mạc. Bệnh nhân bị chấn thương đầu hoặc bỏng cũng gây tăng tiết axit.".split(" ")
    ]
]

results = bleu.compute(predictions=predictions, references=references, max_order = 2)
print(results)
