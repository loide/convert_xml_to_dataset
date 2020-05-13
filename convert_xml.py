import pandas as pd
import xml.etree.ElementTree as et

def parse_XML(xml_file, df_cols):
    xtree = et.parse(xml_file)
    xroot = xtree.getroot()
    rows = []

    for node in xroot:
        if node.tag == "ProductLine_array":
            res = []
            for product_line in node:
                #print(product_line[0].text, product_line[1].text)
                rows.append({df_cols[0]: product_line[0].text, df_cols[1]: product_line[1].text})
                #print(rows)

    out_df = pd.DataFrame(rows, columns=df_cols)

    return out_df

def export_to_excel(df):
    result_file = "_".join(['output', '.xlsx'])
    print('Create file: ', result_file)

    return df.to_excel(result_file, index=None, header=True)

def main():
    filename = 'meliuz02-20-orders.xml'
    #df_columns = ["GLProductGroupID", "ProductGroupName"]
    df_columns = ["category_id", "description"]
    output = parse_XML(filename, df_columns)
    print(output.to_string())

    export_to_excel(output)

if __name__ == "__main__":
    main()
