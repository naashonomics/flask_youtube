import webbrowser
import pandas as pd

def generate_html(dataframe: pd.DataFrame):
    # get the table HTML from the dataframe
    table_html = dataframe.to_html(table_id="table")
    # construct the complete HTML with jQuery Data tables
    # You can disable paging or enable y scrolling on lines 20 and 21 respectively
    html = f"""
    <html>
    <header>
        <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
    </header>
    <body>
    {table_html}
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script>
        $(document).ready( function () {{
            $('#table').DataTable({{
                // paging: false,    
                // scrollY: 400,
            }});
        }});
    </script>
    </body>
    </html>
    """
    # return the html
    return html

def get_data_gen_html():
    df = pd.read_excel('Financial_Sample.xlsx',sheet_name='Sheet1')
    print(df.keys())
    df_enterpise=df[df['Segment'].isin(['Enterprise'])]
    df_cp=df[df['Segment'].isin(['Channel Partners'])]
    df_mm=df[df['Segment'].isin(['Midmarket'])]
    df_gov=df[df['Segment'].isin(['Government'])]
    df_sb=df[df['Segment'].isin(['Small Business'])]
    html = generate_html(df_enterpise)
    open("enterpise.html", "w").write(html)
    webbrowser.open("enterpise.html") 
    html = generate_html(df_cp)
    open("cp.html", "w").write(html)
    webbrowser.open("cp.html")  
    html = generate_html(df_mm)
    open("mm.html", "w").write(html)
    webbrowser.open("mm.html") 
    html = generate_html(df_gov)
    open("gov.html", "w").write(html)
    webbrowser.open("gov.html")      
    html = generate_html(df_sb)
    open("sb.html", "w").write(html)
    webbrowser.open("sb.html")  
if __name__ == "__main__":
	get_data_gen_html()
    