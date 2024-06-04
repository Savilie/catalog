<script setup>
import { onMounted, reactive, ref, watch, provide } from "vue"
import axios from 'axios'

import HeaderSneak from "./components/HeaderSneak.vue"
import CardList from "./components/CardList.vue"
import Drawer from './components/Drawer.vue'

const items = ref([])



const filters = reactive({
  sortBy: 'title',
  searchQuery: ''
})

const searchQuery = ref('')

const onChangeSelect = event => {
  filters.sortBy = event.target.value
}

const fetchFavorites = async () => {
    try {
    const {data: favorites} = await axios.get('https://68ac98afc717bb0e.mokky.dev/favorites')   

    items.value = items.value.map(item => {
      const favorite = favorites.find(favorite => favorite.parentId === item.id)

      if (!favorite) {
        return item
      }

      return {
        ...item,
        isFavorite:true,
        favoriteId: favorite.id,
      }
    })

    } catch(err) {
        console.log(err)
    }  
}

const addToFavorite = async (item) => {

  item.isFavorite = !item.isFavorite

  console.log(item)
}

const onChangeSearchInput = event => {
  filters.searchQuery = event.target.value
}
const fetchItems = async () => {
  try {
    const params = {
      sortBy: filters.sortBy,
    }

    if (filters.searchQuery) {
      params.title = `${filters.searchQuery}`;
    }

    const {data} = await axios.get('http://5.35.85.223/api/catalog/',{
      params
    })   

    items.value = data.map(obj => ({
      ...obj,
      isFavorite: false,
      isAdded:false      
    }))
    console.log(items.value)

    } catch(err) {
        console.log(err)
    }  
}

onMounted(async () => {
  await fetchItems();
  await fetchFavorites();
})

watch(filters, fetchItems)

provide('addToFavorite', addToFavorite)
</script>



<template>
  <!-- <Drawer /> -->
  <div class="w-4/5 m-auto bg-white rounded-xl shadow-xl mt-14">
    <HeaderSneak />

    <div class="p-10">
      <div class="flex justify-between items-center">
        <h2 class="text-3xl font-bold mb-10">Все кроссовки</h2>

        <div class="flex gap-4">
          <select @change="onChangeSelect" class="py-1.5 px-3 border rounded-md outline-none focus:border-gray-400 transition">
            <option value="name">По названию</option>
            <option value="price">По цене (возрастанию)</option>
            <option value="-price">По цене (убыванию)</option>
          </select>

        <div class="relative">
        <img class="absolute top-2.5 left-4" src="/search.svg">
        <input @input="onChangeSearchInput" class="border rounded-md py-1.5 pl-11 pr-4 outline-none focus:border-gray-400 transition" type="text" placeholder="Поиск">          
        </div>
        </div>
      </div>

      <div class="mt-10">
            <CardList :items="items"/>
      </div>

    </div>

  </div>
</template>