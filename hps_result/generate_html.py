def generate_comparison_html(models, base_path, img_path, input_sizes):
    # 表格的行动态生成
    tables = ""
    for input_size in input_sizes:
        table = f"""
        <h2 class="text-center">Input Size: {input_size}</h2>
        <table class="table table-bordered">
            <thead class="table-dark">
                <tr>
                    <th>Original</th>
                    {"".join([f"<th>Model {model}</th>" for model in models])}
                </tr>
            </thead>
            <tbody>
        """

        # 遍历 ./img 文件夹的所有图片
        for image in img_path.glob("*.jpg"):
            row = f"<tr><td><img src='{image}' title='{image}' alt='{image}' class='img-thumbnail'></td>"

            for model in models:
                # 推理结果图片路径
                inference_image = base_path / f"model_{model}" / str(input_size) / image.name
                if inference_image.exists():
                    row += f"<td><img src='{inference_image}' title='{inference_image}' alt='Model {model}' class='img-thumbnail'></td>"
                else:
                    row += f"<td>Image not found {inference_image}</td>"

            row += "</tr>"
            table += row

        table += "</tbody></table>"
        tables += table

    # HTML 模板
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Model Comparison</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            table {{ text-align: center; }}
            img {{ max-width: 100%; height: auto; }}
        </style>
    </head>
    <body>
        <div class="container my-5">
            <h1 class="text-center">Model Comparison</h1>
            <p class="text-center">Comparison of different models for the same input size</p>
            {tables}
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

    # 将 HTML 写入文件
    with open("comparison.html", "w") as f:
        f.write(html_template)
    print("HTML file 'comparison.html' generated successfully.")

def generate_comparison_table(model, base_path, original_img_path, input_sizes):
    # 获取原始图片列表
    original_images = list(original_img_path.glob("*.jpg"))

    # 开始构建 HTML 表格
    rows = ""
    for img in original_images:
        row = f"<tr><td><img src='./img/{img.name}' alt='Original' style='max-width:100%; height:auto;'></td>"
        for input_size in input_sizes:
            # 推理图片路径
            dir_path = base_path / f"model_{model}" / str(input_size)
            result_img_path = dir_path / img.name
            if result_img_path.exists():
                row += f"<td><img src='{result_img_path}' title='{result_img_path}' alt='{input_size}' style='max-width:100%; height:auto;'></td>"
            else:
                row += f"<td>Image not found</td>"
        row += "</tr>"
        rows += row

    # 完整 HTML 模板
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Model {model} Comparison</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            table {{ text-align: center; width: 100%; }}
            img {{ max-width: 100%; height: auto; }}
        </style>
    </head>
    <body>
        <div class="container my-5">
            <h1 class="text-center">Model {model} Comparison</h1>
            <p class="text-center">Comparison of different input sizes for the same images</p>
            <div class="table-responsive">
                <table class="table table-bordered">
                    <thead class="table-dark">
                        <tr>
                            <th>Original Image</th>
                            <th>Input Size 192</th>
                            <th>Input Size 256</th>
                            <th>Input Size 512</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rows}
                    </tbody>
                </table>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

    # 将 HTML 写入文件
    with open(f"model_{model}_comparison.html", "w") as f:
        f.write(html_template)
    print(f"HTML file 'model_{model}_comparison.html' generated successfully.")

def generate_comparison_html_1(models, base_path, img_path, input_sizes):
    # 检查原始图片文件夹是否存在
    if not img_path.exists():
        print(f"Image folder not found: {img_path}")
        return

    # 生成 HTML 表格内容
    table_rows = ""
    for image in img_path.glob("*.jpg"):  # 遍历原始图片
        for model in models:  # 每个模型换一行
            row = f"<tr><td>{model}</td><td><img src='{image}' alt='Original' class='img-thumbnail'></td>"  # 第一列为模型名称，第二列为原始图片
            for input_size in input_sizes:
                # 拼接推理图片路径
                inference_image = base_path / f"model_{model}" / str(input_size) / image.name
                # 检查推理图片是否存在
                if inference_image.exists():
                    row += f"<td><img src='{inference_image}' alt='Model {model}, Size {input_size}' class='img-thumbnail'></td>"
                else:
                    row += "<td>Image not found</td>"  # 如果图片不存在，显示占位
            row += "</tr>"
            table_rows += row

    # HTML 模板
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Model Comparison</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            table {{ text-align: center; }}
            img {{ max-width: 100%; height: auto; }}
        </style>
    </head>
    <body>
        <div class="container my-5">
            <h1 class="text-center">Model and Input Size Comparison</h1>
            <p class="text-center">Comparison of different models for the same image across different input sizes</p>
            <table class="table table-bordered">
                <thead class="table-dark">
                    <tr>
                        <th>Model</th>
                        <th>Original</th>
                        {"".join([f"<th>Input Size {size}</th>" for size in input_sizes])}
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

    # 保存 HTML 文件
    with open("comparison_1.html", "w") as f:
        f.write(html_template)
    print("HTML file 'comparison_1.html' generated successfully.")

def generate_comparison_html_2(models, base_path, img_path, input_sizes):
    # 检查原始图片文件夹是否存在
    if not img_path.exists():
        print(f"Image folder not found: {img_path}")
        return

    # 生成 HTML 表格内容
    table_rows = ""
    for image in img_path.glob("*.jpg"):  # 遍历原始图片
        table_rows += f"<tr><td rowspan='{len(input_sizes)}'><img src='{image}' alt='Original' class='img-thumbnail'></td>"  # 第一列为原始图片，并跨多行

        # 为每个输入尺寸生成一行
        for idx, input_size in enumerate(input_sizes):
            row = "" if idx == 0 else "<tr>"  # 第一行已经开始，后续行用新 `<tr>`
            row += f"<td>Input Size {input_size}</td>"  # 第二列为输入尺寸
            for model in models:
                # 拼接推理图片路径
                inference_image = base_path / f"model_{model}" / str(input_size) / image.name
                # 检查推理图片是否存在
                if inference_image.exists():
                    row += f"<td><img src='{inference_image}' alt='Model {model}, Size {input_size}' class='img-thumbnail'></td>"
                else:
                    row += "<td>Image not found</td>"  # 如果图片不存在，显示占位
            row += "</tr>"
            table_rows += row

    # HTML 模板
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Model Comparison</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            table {{ text-align: center; }}
            img {{ max-width: 100%; height: auto; }}
        </style>
    </head>
    <body>
        <div class="container my-5">
            <h1 class="text-center">Model and Input Size Comparison</h1>
            <p class="text-center">Comparison of the same image across different models and input sizes</p>
            <table class="table table-bordered">
                <thead class="table-dark">
                    <tr>
                        <th>Original</th>
                        <th>Input Size</th>
                        {"".join([f"<th>Model {model}</th>" for model in models])}
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

    # 保存 HTML 文件
    with open("comparison_1.html", "w") as f:
        f.write(html_template)
    print("HTML file 'comparison_1.html' generated successfully.")