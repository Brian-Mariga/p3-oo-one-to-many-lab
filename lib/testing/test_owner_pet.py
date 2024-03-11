import pytest
from owner_pet import Pet, Owner

def test_owner_init():
    """Test Owner class initialization"""
    owner = Owner("John")
    assert owner.name == "John"

def test_pet_init():
    """Test Pet class initialization"""
    pet = Pet("Fido", "dog")
    assert pet.name == "Fido"
    assert pet.pet_type == "dog"

    owner = Owner("Jim")
    pet = Pet("Clifford", "dog", owner)
    assert pet.owner == owner

    Pet.all = []

def test_has_pet_types():
    """Test Pet class has variable PET_TYPES"""
    assert Pet.PET_TYPES == ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    Pet.all = []

def test_checks_pet_type():
    """Test Pet class validates pet_type"""
    with pytest.raises(Exception):
        Pet("Jim Jr.", "panda")

    Pet.all = []

def test_pet_has_all():
    """Test Pet class has variable all, storing all instances of Pet"""
    pet1 = Pet("Whiskers", "cat")
    pet2 = Pet("Jerry", "reptile")

    assert pet1 in Pet.all
    assert pet2 in Pet.all
    assert len(Pet.all) == 2

    Pet.all = []


def test_owner_adds_pets():
    """Test Owner class has method add_pet(), validating and adding a pet"""
    owner = Owner("Ben")
    pet = Pet("Whiskers", "cat")
    owner.add_pet(pet)

    assert pet.owner == owner
    assert owner.pets() == [pet]

    Pet.all = []

def test_add_pet_checks_isinstance():
    """Test Owner class instance method add_pet() validates Pet type"""
    owner = Owner("Jim")
    with pytest.raises(Exception):
        owner.add_pet("Lucky")

    Pet.all = []

