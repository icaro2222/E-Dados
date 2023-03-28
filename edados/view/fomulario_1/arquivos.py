
        Dataframe = Microdado_Amostra.sort_values(by=[filtro_questao])
        # Dataframe.reset_index()
        # pd.set_option("max_colwidth", 2)
        pd.set_eng_float_format(accuracy=6, use_eng_prefix=True)

        # Dataframe = Dataframe.groupby(filtro_questao).agg({
        #     "NU_IDADE":("count")
        # })

        Dataframe1 = Dataframe.groupby(filtro_questao)['NU_IDADE']
        Dataframe = Dataframe.groupby(filtro_questao)

        Dataframe = Dataframe.describe().T
        Dataframe1 = Dataframe1.describe()
        # Dataframe = Dataframe['NU_IDADE']

        # rotacionar 
        # Dataframe = Dataframe.unstack()

        # lista_dos_index = Dataframe['A']
        # print(lista_dos_index)

        # desrotacionar 
        # Dataframe = Dataframe.stack()


        # pd.set_option('display.max_colwidth',4)
        # teste = Dataframe['A'].apply(formatar)
        
        # print(Dataframe['count']) 
        
        figura_tabela_da_media = px.bar(Dataframe['count'])
        Dataframe = figura_tabela_da_media.to_html()

        # Dataframe = Dataframe.to_html()   

        relatorio_em_tabela = Dataframe1.to_html(
            max_rows=10, justify='center', 
            classes="""table table-striped table-bordered table-sm
            text-dark"""
            )

        figura_tabela = px.line(Dataframe.index, Dataframe)

        relatorio_em_tabela = figura_tabela.to_html()
