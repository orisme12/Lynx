import { createClient } from 'https://esm.sh/@supabase/supabase-js@2.39.0'
import { load } from 'deps/lib.ts'

const env = await load()
const SUPABASE_URL = env['SUPABASE_URL']
const SUPABASE_KEY = env['SUPABASE_KEY']
const supabase = createClient(SUPABASE_URL, SUPABASE_KEY)

export default supabase
