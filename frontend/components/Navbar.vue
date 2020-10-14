<template>
  <div>
    <b-navbar toggleable="lg" type="light" variant="light">
      <b-navbar-brand href="#">Дневник тренировок</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item href="#">Главная</b-nav-item>
          <b-nav-item href="#">Блог</b-nav-item>
          <b-nav-item href="#">Все тренировки</b-nav-item>
          <b-nav-item active href="#">Мои тренировки</b-nav-item>
          <b-nav-item href="#">Упражения</b-nav-item>
          <b-nav-item href="#">Статистика</b-nav-item>
          <b-nav-item href="#">Замеры</b-nav-item>
          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>Аккаунт</em>
            </template>
            <b-dropdown-item href="#">Профиль</b-dropdown-item>
            <b-dropdown-item href="#">Выйти</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

