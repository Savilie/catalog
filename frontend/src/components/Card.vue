<script setup>
import {inject} from 'vue'

defineProps({
  id:Number,
  imageUrl: String,
  title: String,
  price: Number,
  isFavorite: Boolean,
  isAdded: Boolean,
  onClickFavorite: Function,
  onClickAdd:Function
})

</script>


<template>

      <div class="bg-white relative border border-slate-100 rounded-3xl p-8 cursor-pointer transition hover:-translate-y-2 hover:shadow-xl">
        <img :src="'http://5.35.85.223' + imageUrl" alt="Sneaker" />

        <p class="mt2">{{ title }}</p>

        <div class="flex justify-between mt-5">
          <div class="flex flex-col">
            <span class="text-slate-400">Цена:</span>
            <b>{{ price }} руб.</b>
          </div>

        </div>
      </div>

</template>