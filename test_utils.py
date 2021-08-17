import pytest
import utils

@pytest.fixture
def initial_site():
    return 'https://www.monark.com.pe/categoria-producto/bicicletas/'

@pytest.fixture
def initial_n_page_site():
    return 'https://www.monark.com.pe/categoria-producto/bicicletas/?page=3'

def test_extract_domain_from_url():
    assert utils.extract_domain_from_url('https://www.monark.com.pe/categoria-producto/bicicletas/?page=3') == 'www.monark.com.pe' 

def test_ensure_absolute_url_from_absolute(initial_n_page_site):
    assert utils.ensure_absolute_url(initial_n_page_site, 'https://www.monark.com.pe/categoria-producto/bicicletas/') == 'https://www.monark.com.pe/categoria-producto/bicicletas/'

def test_ensure_absolute_url_from_relative_initial_site(initial_site):
    assert utils.ensure_absolute_url(initial_site, '?page=4') == 'https://www.monark.com.pe/categoria-producto/bicicletas/?page=4'

def test_ensure_absolute_url_from_relative_initial_n_site(initial_n_page_site):
    assert utils.ensure_absolute_url(initial_n_page_site, '?page=4') == 'https://www.monark.com.pe/categoria-producto/bicicletas/?page=4'

def test_ensure_absolute_url_from_empty_string(initial_site):
    assert utils.ensure_absolute_url(initial_site, '') == ''