class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self,name,pet_type,owner = None):
        if pet_type not in Pet.PET_TYPES: #validation
            raise ValueError(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
     #add new isnatnce to the list of all pets
        Pet.all.append(self)
        


class Owner:
  def __init__(self, name):
      self.name = name


  def pets(self):
      return [pet for pet in Pet.all if pet.owner == self]
  
  

  def add_pet(self, pet):
      # check type 
      if isinstance(pet, Pet):
          #assign the owner to the pet
          pet.owner = self

      else:
        raise TypeError("Expected a Pet instance")
              
    
  def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
      