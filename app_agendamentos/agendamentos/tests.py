from django.test import TestCase
from .forms import DadosForm
from django.utils import timezone

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

from django.test import TestCase
from .models import DadosGerais
from datetime import datetime

class DadosGeraisModelTest(TestCase):
    
    def setUp(self):
        """Cria um objeto de teste no banco de dados"""
        self.dados = DadosGerais.objects.create(
            codigo_treinamento=123,
            treinamento="Treinamento Django",
            docente="Professor X",
            proposta="Proposta ABC",
            empresa="Empresa XYZ",
            cliente="Cliente 1",
            status="ANDAMENTO",
            data_inicial=timezone.make_aware(datetime(2025, 3, 11, 8, 0, 0)),
            data_final=timezone.make_aware(datetime(2025, 3, 15, 17, 0, 0)),
            dias_treinamento=5,
            turno="Manhã",
            horas=timezone.make_aware(datetime(2025, 3, 11, 8, 0, 0)),
            observacao="Nenhuma observação"
        )

    def test_dados_gerais_creation(self):
        """Testa se o objeto foi salvo corretamente no banco"""
        dados = DadosGerais.objects.get(codigo_treinamento=123)
        self.assertEqual(dados.treinamento, "Treinamento Django")
        self.assertEqual(dados.docente, "Professor X")
        self.assertEqual(dados.proposta, "Proposta ABC")
        self.assertEqual(dados.empresa, "Empresa XYZ")
        self.assertEqual(dados.cliente, "Cliente 1")
        self.assertEqual(dados.status, "ANDAMENTO")
        self.assertEqual(dados.data_inicial, timezone.make_aware(datetime(2025, 3, 11, 8, 0, 0)))
        self.assertEqual(dados.data_final, timezone.make_aware(datetime(2025, 3, 15, 17, 0, 0)))
        self.assertEqual(dados.dias_treinamento, 5)
        self.assertEqual(dados.turno, "Manhã")
        self.assertEqual(dados.horas, timezone.make_aware(datetime(2025, 3, 11, 8, 0, 0)))
        self.assertEqual(dados.observacao, "Nenhuma observação")

    def test_str_method(self):
        """Testa se o método __str__ do modelo está retornando corretamente"""
        self.assertEqual(str(self.dados), "Treinamento Django - 123")
