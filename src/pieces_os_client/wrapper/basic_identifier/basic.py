from abc import ABC,abstractmethod
from typing import  Optional
from pieces_os_client import Annotations, AnnotationTypeEnum


class Basic(ABC):
	def __init__(self, id) -> None:
		"""
		Initialize the class with a given ID.

		:param id: The ID of the Object.
		"""
		self._id = id

	@property
	def description(self) -> Optional[str]:
		"""
		Retrieve the description.

		:return: The description text or None if not available.
		"""
		annotations = self.annotations
		if not annotations:
			return
		d = None
		for annotation in annotations.iterable:
			if annotation.type == AnnotationTypeEnum.DESCRIPTION:
				d = annotation
		
		return d.text if d else None

	@property
	@abstractmethod
	def annotations(self)  -> Optional[Annotations]:
		"""
		Get all the annotations.

		Returns:
			Optional[Annotations]: The annotations if available, otherwise None.
		"""
		pass

	@property
	@abstractmethod
	def id(self) -> str:
		pass

	@abstractmethod
	def delete(self) -> None:
		pass

	def __repr__(self):
		"""
		Returns a detailed string representation of the object.
		"""
		return f"<{self.__class__.__name__}(id={self.id})>"

	def __eq__(self, other):
		"""
		Checks equality between two instances.
		"""
		if isinstance(other, self.__class__):
			return self.id == other.id
		return False

	def __str__(self):
		"""
		Returns a user-friendly string representation of the object.
		"""
		if hasattr(self,"name"):
			return f"ID: {self.id}, Name: {self.name}"
		return f"ID: {self.id}"


	def __hash__(self):
		"""
		Returns a hash of the instance.
		"""
		return hash(self.id)

