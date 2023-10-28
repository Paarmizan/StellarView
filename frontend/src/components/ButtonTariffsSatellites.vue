<template>
  <button class="btn">
    <slot></slot>
  </button>
</template>

<script>
export default {
name: "butTS"
}
</script>

<style lang="scss" scoped>
*{
  background: black;
}
button{
  width: 330px;
  height: 90px;
  background: transparent;
  border: 3px solid white;
  border-radius: 19px;
  font-size: 36px;
  top: 140px;
  left: 40px;
  position: absolute;
  color: white;
  margin-left: 60px;

  transition: 0.3s border-color, transform 0.3s, color 0.3s;


  &:hover {
    border-color: #15C6E9;
    transform: scale(1.1);
    color: #15C6E9;
  }
}
</style>