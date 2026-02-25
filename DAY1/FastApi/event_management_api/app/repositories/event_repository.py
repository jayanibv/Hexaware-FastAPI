class EventRepository:
    def __init__(self):
        self._events = []
        self._counter = 1

    def save(self, event_data: dict):
        event_data["id"] = self._counter
        self._events.append(event_data)
        self._counter += 1
        return event_data

    def find_all(self):
        return self._events

    def find_by_id(self, event_id: int):
        return next((e for e in self._events if e["id"] == event_id), None)

    def find_by_location(self, location: str):
        return [e for e in self._events if e["location"].lower() == location.lower()]

    def find_by_name(self, name: str):
        return next((e for e in self._events if e["name"].lower() == name.lower()), None)