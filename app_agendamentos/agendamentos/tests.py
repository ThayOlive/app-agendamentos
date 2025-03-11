from django.test import TestCase
from .forms import DadosForm

class DadosFormTest(TestCase):

    def test_form_fields_exist(self):
        """Testa se todos os campos do formulário estão presentes"""
        form = DadosForm()
        expected_fields = [
            "codigo_treinamento", "treinamento", "docente", "proposta",
            "empresa", "cliente", "status", "data_inicial", "data_final",
            "dias_treinamento", "turno", "horas", "observacao"
        ]
        
        # Verifica se todos os campos estão no formulário
        for field in expected_fields:
            self.assertIn(field, form.fields)

    def test_status_choices_present(self):
        """Testa se as opções do campo status estão corretas"""
        form = DadosForm()
        status_field = form.fields["status"]
        expected_choices = [
            ("ANDAMENTO", "Em andamento"),
            ("CONCLUÍDO", "Concluído"),
        ]
        self.assertEqual(status_field.choices, expected_choices)

    def test_form_is_valid_with_valid_data(self):
        """Testa se o formulário é válido quando todos os dados estão corretos"""
        valid_data = {
            "codigo_treinamento": 123,
            "treinamento": "Treinamento Django",
            "docente": "Professor X",
            "proposta": "Proposta ABC",
            "empresa": "Empresa XYZ",
            "cliente": "Cliente 1",
            "status": "ANDAMENTO",
            "data_inicial": "2025-03-11 08:00:00",  # Formato correto de data/hora
            "data_final": "2025-03-15 17:00:00",
            "dias_treinamento": 5,
            "turno": "Manhã",
            "horas": "2025-03-11 08:00:00",  # Corrigido para data/hora válida
            "observacao": "Nenhuma observação",
        }

        form = DadosForm(data=valid_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_with_missing_fields(self):
        """Testa se o formulário é inválido quando campos obrigatórios estão ausentes"""
        invalid_data = {
            "codigo_treinamento": 123,  # Deixando outros campos vazios
        }
        form = DadosForm(data=invalid_data)
        self.assertFalse(form.is_valid())
