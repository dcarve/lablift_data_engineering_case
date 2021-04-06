# labfit_data_engineering_case

## Observações:

- Eu não tenho experiência com scikit-learn, então levei um tempo para entender a classe sklearn.pipeline.Pipeline e  como usá-la. O que dificultou foi não saber qual era o tipo de entrada que deveria ser utilizada na classe para obter a predição, embora fosse implicíto, como não tenho experiência, levei um tempo para compreender qual entrada deveria ser usada, e qual o formato.

- Minha intensão era usar wsgi na API, para facilitar a documentação, mas os modelos que eu tinha disso eu fiz no meu trabalho, e não fiz uma cópia para meu repositório pessoal, então tive que fazer uma api mais simples.


## API

###### Endpoint
http://localhost:5500/donation
###### Método
POST
###### Headers
{"Content-Type":"application/json"}
###### Body
{"patient_id":numero_do_id_paciente}

exemplo

{"patient_id":439}





