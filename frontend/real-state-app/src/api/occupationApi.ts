import api from "./api";

export const occupationsApi = {
  async getAll() {
    const res = await api.get("/occupations");
    return res.data;
  },

  async getById(id: number) {
    const res = await api.get(`/occupations/${id}`);
    return res.data;
  },

  async create(data: unknown) {
    const res = await api.post("/occupations", data);
    return res.data;
  },

  async update(id: number, data: unknown) {
    const res = await api.put(`/occupations/${id}`, data);
    return res.data;
  },

  async delete(id: number) {
    const res = await api.delete(`/occupations/${id}`);
    return res.data;
  },

};